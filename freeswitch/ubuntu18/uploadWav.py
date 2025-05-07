from flask import Flask, jsonify,request
import logging
import os
import boto3
from datetime import datetime
import threading

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
app = Flask(__name__)

# S3 配置
S3_URL= os.getenv('S3_URL')
S3_ACCESS_KEY = os.getenv('S3_ACCESS_KEY')
S3_SECRET_KEY = os.getenv('S3_SECRET_KEY')
S3_REGION = os.getenv('S3_REGION')
S3_BUCKET = os.getenv('S3_BUCKET')

# 初始化 S3 客户端
s3_client = boto3.client(
    's3',
    aws_access_key_id=S3_ACCESS_KEY,
    aws_secret_access_key=S3_SECRET_KEY,
    region_name=S3_REGION,
    endpoint_url=S3_URL,
    use_ssl=False,
    verify=False
)

def uploadToS3(audio_path: str, filename: str):
    s3_client.upload_file(audio_path, S3_BUCKET, filename)
    # 删除临时文件
    os.remove(audio_path)

@app.route('/audio',methods=['POST'])
def get_audio():
    return_data = {}
    data = request.get_json()
    audio_path = data['path']
    logging.info(audio_path)
    if not audio_path:
        return jsonify({'error': 'No audio path provided'}), 400

    if not os.path.exists(audio_path):
        return jsonify({'error': 'Audio file not found'}), 404
    # 获取当前日期并格式化为 "YYYY-MM-DD" 格式
    current_date = datetime.now().strftime('%Y-%m-%d')
    # 获取文件名
    filename = current_date + "/" + os.path.basename(audio_path)
    # 上传到 S3
    try:
        # 在后台线程中执行长时间任务，不阻塞主线程
        thread = threading.Thread(target=uploadToS3, args=(audio_path, filename))
        thread.start()
        print("145667889")
        return jsonify({"msg": "File uploaded successfully", "code": 200, "data": "s3://" + S3_BUCKET + "/" + filename}), 200
    except Exception as e:
        return jsonify({"msg": f"File uploaded Failed: {str(e)}", "code": 500}), 500

if __name__ == '__main__':
    port = int(os.getenv('FS_RECORD_PORT', 28080))
    app.run(host='0.0.0.0',port=port, debug=False)

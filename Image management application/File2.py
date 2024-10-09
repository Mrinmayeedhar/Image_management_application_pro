from flask import Flask, render_template, request, redirect, url_for
import boto3
import os

app = Flask(__name__)

# AWS S3 Setup
s3 = boto3.client('s3')
BUCKET_NAME = 'imagescreatedbyme'

# Home page to upload image
@app.route('/')
def home():
    return render_template('upload.html')

# Upload image to S3
@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return "No file part"
    
    file = request.files['file']
    if file.filename == '':
        return "No selected file"
    
    if file:
        s3.upload_fileobj(file, BUCKET_NAME, file.filename)
        return redirect(url_for('list_images'))

# List images from S3
@app.route('/images')
def list_images():
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)
    if 'Contents' in response:
        images = [obj['Key'] for obj in response['Contents']]
    else:
        images = []
    
    return render_template('list.html', images=images)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

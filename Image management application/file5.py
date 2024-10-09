@app.route('/download/<filename>', methods=['GET'])
def download_image(filename):
    obj = s3.get_object(Bucket=BUCKET_NAME, Key=filename)
    encrypted_data = obj['Body'].read()

    decrypted_data = cipher_suite.decrypt(encrypted_data)

    with open(f'/tmp/{filename}', 'wb') as f:
        f.write(decrypted_data)

    return send_file(f'/tmp/{filename}', as_attachment=True)

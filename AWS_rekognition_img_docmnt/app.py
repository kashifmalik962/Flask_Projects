from flask import Flask, render_template, request
import boto3
from botocore.exceptions import ClientError

app = Flask(__name__)

# AWS credentials
AWS_ACCESS_KEY = 'AKIA3M55JFJQLX4WSTTC'
AWS_SECRET_KEY = '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'
AWS_REGION = 'us-east-1'

# Initialize AWS Rekognition client
rekognition = boto3.client('rekognition',
                           aws_access_key_id=AWS_ACCESS_KEY,
                           aws_secret_access_key=AWS_SECRET_KEY,
                           region_name=AWS_REGION)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/label', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['file']
        selected_option = request.form['action']
        
        # Process the uploaded image with AWS Rekognition for label detection
        if selected_option == 'option1':
            response_labels = rekognition.detect_labels(
                Image={
                    'Bytes': file.read()
                },
                MaxLabels=10
            )

                # Return JSON response for label detection to the client-side
            return render_template('label.html',response_labels=response_labels)
        
        elif selected_option == 'option2':
            response_faces = rekognition.detect_faces(
                Image={
                    'Bytes': file.read()
                },Attributes=["ALL"]
                )
            return render_template('label.html', response_faces=response_faces)
        
        elif selected_option == 'option3':
            response_text = rekognition.detect_text(
                Image={
                    'Bytes': file.read()
                })
            
            return render_template('label.html', response_text=response_text)
        
        elif selected_option == 'option4':
            response_celebrities = rekognition.recognize_celebrities(
                Image={
                    'Bytes': file.read()
                },Attributes=["ALL"]
                )
            
            return render_template('label.html', response_celebrities=response_celebrities)
    else:
        return render_template('label.html')





# @app.route('/face_detect', methods=['POST'])
# def detect_face():
#     if request.method == 'post':
#         try:
#             # Retrieve the image file for face detection
#             file_for_face_detection = {'Bytes': file.read()}

#             response_faces = rekognition.detect_faces(
#                 Image={
#                     'Bytes': file_for_face_detection.read()
#                 },
#                 Attributes=["ALL"]
#             )

#             # Extract faces data
#             faces = response_faces['FaceDetails']

#             # Render the results in result.html for face detection
#             return render_template('result.html', response_faces=faces)
#         except ClientError as e:
#             # Handle errors for face detection
#             error_message = f"An error occurred: {e.response['Error']['Message']}"
#             return error_message
#     return render_template()

if __name__ == '__main__':
    app.run(debug=True)
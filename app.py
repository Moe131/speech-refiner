from flask import Flask, render_template, request, redirect, flash, session
import uuid
import os
from refiner import *

UPLOAD_FOLDER = 'recordings'
PREVIOUS_CHATS_FOLDER = 'chats'


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = 'supersecretkey'  # Needed for session and flash messages

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        # Get the refined text from the session, defaulting to an empty string if not set
        refined_text = session.get('refined_text', '')
        return render_template('index.html',lines=refined_text.split("\n"))
    
    if request.method == 'POST':
        if 'file' not in request.files:
            flash("No file uploaded")
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # Generate a unique filename and save the uploaded file
        file_name = str(uuid.uuid4()) + ".mp3"
        full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(full_file_name)
        
        # Call the refine function to process the uploaded file
        transcript = voice_to_text(full_file_name)
        refined_text = refine(transcript)
        chat = save_chat(full_file_name,transcript, refined_text)
        session['refined_text'] = chat  # Store the result in the session
        # Redirect to the main page to display the refined text
        return render_template('index.html', lines=refined_text.split("\n"))

if __name__ == "__main__":
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    os.makedirs(PREVIOUS_CHATS_FOLDER, exist_ok=True)
    app.run()

from cmu_graphics import *
from flask import Flask, request, jsonify
import os
import json
from werkzeug.utils import secure_filename
from PIL import Image
import uuid
def dragAndDrop(app):
    app = Flask(__name__)

    app.config["imageFolder"] = 'images'
    app.config['allowedExtensions'] = {'png', 'jpg', 'jpeg'}
    closetFile = 'closet.json'

    def allowedFile(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['allowedExtensions']

    # Load closet data from JSON
    def loadClosetData():
        if os.path.exists(closetFile):
            with open(closetFile, 'r') as file:
                return json.load(file)
        else:
            return {'tops': [], 'bottoms': []}

    # Save closet data to JSON
    def saveClosetData():
        closetData = {'tops': app.tops, 'bottoms': app.bottoms}
        with open(closetFile, 'w') as file:
            json.dump(closetData, file)

    # Initialize app lists from the JSON file
    closetData = loadClosetData()
    app.tops = closetData['tops']
    app.bottoms = closetData['bottoms']

    # Route for uploading files
    @app.route('/upload', methods=['POST'])
    def uploadImage():
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        
        image = request.files['image']
        if image.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        
        if image and allowedFile(image.filename):
            img = Image.open(image.stream)
            img = img.convert("RGBA")

            # Save the image to the appropriate folder
            filename = secure_filename(f'{uuid.uuid4().hex}.png')
            filepath = os.path.join(app.config['imageFolder'], filename)
            image.save(filepath, 'PNG')

            # Add image to the correct list based on the current category
            if app.category == 'top':
                app.tops.append(filepath)
            elif app.category == 'bottom':
                app.bottoms.append(filepath)
            else:
                return jsonify({'error': 'No valid category set'}), 400

        # Save the updated closet data to the JSON file
        saveClosetData()
        return jsonify({
            'message': f'Image uploaded to {app.category} category',
            'imagePath': filepath
        }), 200
    return jsonify({'error': 'Invalid file type'}), 400
    

   



        

#     #Background
#     def importModeBackground(app):
#         drawImage("images/importModeBackground.jpeg", 0, 0, width=app.width,
#                 height=app.height)
#         drawRect(app.width/2, app.height/2, 200, 200, fill="white")
#         drawTopButton(app)
#         drawBottomButton(app)
#         drawLabel("select if you are uploading a top or bottom")


# app.topButtonX = 300
# app.topButtonY = 200
# app.bottomButtonX = 300
# app.bottomButtonY = 400

# def drawTopButton(app):
#     drawRect(app.topButtonX, app.topButtonY, 100, 50, fill="lightblue")
#     drawLabel("Top", app.topButtonX, app.topButtonY, size=20,)
# def pressTopButton(app):
#     if (app.topButtonX <= app.mouseX <= app.topButtonX+100 and 
#         app.topButtonY <= app.mouseY <= app.topButtonY+50):
#        pass
#        #add pic to tops list

# def drawBottomButton(app):
#     drawRect(app.bottomButtonX, app.bottomButtonY, 100, 50, fill="lightblue")
#     drawLabel("Bottom", app.bottomButtonX, app.bottomButtonY, size=20,)
# def pressBottomButton(app):
#     if (app.bottomButtonX <= app.mouseX <= app.bottomButtonX+100 and 
#         app.bottomButtonY <= app.mouseY <= app.bottomButtonY+50):
#        pass
#        #add pic to bottoms list

    app.category = 'top'
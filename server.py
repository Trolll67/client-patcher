import os
from flask import Flask, abort, send_file

app = Flask(__name__)

base_path = 'Patches/Korea' # path to patches

# return lastest patch version
@app.route('/r2/service/R2VerData.dat')
def serve_version_file():
    return send_file(f'{base_path}/R2VerData.dat', mimetype='application/octet-stream')

# return patch files
@app.route('/r2/service/Patch_<int:id>/<filename>')
def serve_file(id, filename):
    file_path = f'{base_path}/Patch_{id}/{filename}'
    
    if os.path.exists(file_path):
        return send_file(file_path, mimetype='application/octet-stream')
    else:
        abort(404, description=f"File not found")

if __name__ == '__main__':
    app.run(host='localhost', port=8000)
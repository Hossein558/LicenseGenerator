from flask import Flask, request, render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    crm_org_name = os.environ.get('CRM_ORG_NAME', 'tesnaco.com')
    return render_template('index.html', crm_org_name=crm_org_name)

@app.route('/generate')
def generate():
    org = request.args.get('o')
    plugin = request.args.get('p')
    
    if not org or not plugin:
        return "Missing parameters 'o' or 'p'", 400

    # Command construction based on user requirements
    # java -jar atlassian-agent.jar -d -m hossein_ebrahimi_@outlook.com -o <ORG> -p <PLUGIN> -s BLR3-21FQ-DOAO-72QZ
    cmd = [
        "java", "-jar", "atlassian-agent.jar",
        "-d",
        "-m", "hossein_ebrahimi_@outlook.com",
        "-o", org,
        "-p", plugin,
        "-s", "BLR3-21FQ-DOAO-72QZ"
    ]
    
    try:
        # Run command and capture output
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8')
        
        # Filter out banner lines (starting with =)
        lines = result.splitlines()
        filtered_lines = [line for line in lines if not line.strip().startswith('=')]
        
        return '\n'.join(filtered_lines).strip()
    except subprocess.CalledProcessError as e:
        return f"Error executing jar: {e.output.decode('utf-8')}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

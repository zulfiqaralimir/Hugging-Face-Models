To use endpoints of Hugging Face's LLMs (Language Models) in your Streamlit app, you'll need to interact with the Hugging Face Inference API, which allows you to make HTTP requests to use pre-trained models hosted on Hugging Face's platform.

Here’s how you can set up your environment and create a Streamlit app to interact with Hugging Face LLM endpoints:

### 1. Set up a Virtual Environment (Optional but Recommended)

```bash
# Navigate to your project directory
cd /path/to/your/project

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 2. Install Required Packages

```bash
# Install Streamlit
pip install streamlit

# Install requests to make HTTP calls to Hugging Face API
pip install requests
```

### 3. Create a Hugging Face Account and Obtain API Token

1. Go to the [Hugging Face website](https://huggingface.co/).
2. Sign up or log in to your account.
3. Go to your profile settings and generate an API token.

### 4. Create a Streamlit App Using Hugging Face Endpoints

Here’s a simple example:

```python
# app.py

import streamlit as st
import requests

# Set your Hugging Face API token
openai-community/gpt2
mistralai/Mistral-Nemo-Instruct-2407
meta-llama/Meta-Llama-3.1-8B-Instruct
API_URL = "https://api-inference.huggingface.co/models/openai-community/gpt2"

API_URL = "https://api-inference.huggingface.co/models/gpt2"
API_TOKEN = "your_hugging_face_api_token"

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

st.title("Hugging Face LLM Endpoint with Streamlit")

# Text input for the user
user_input = st.text_input("Enter a prompt:")

if user_input:
    # Query the model via the API
    output = query({"inputs": user_input})

    # Display the generated text
    st.write("Generated text:")
    st.write(output[0]["generated_text"])
```

## Note

def query(payload):
response = requests.post(API_URL, headers=headers, json=payload)
return response.json()

data = {"inputs": "Once upon a time,"}
output = query(data)

# Print the output to see what is being returned

st.write(output)

# Safely attempt to access the generated text

if isinstance(output, list) and len(output) > 0 and "generated_text" in output[0]:
st.write(output[0]["generated_text"])
else:
st.write("No generated text found in the response.")

{
"error":"The model meta-llama/Meta-Llama-3-8B is too large to be loaded automatically (16GB > 10GB). Please use Spaces (https://huggingface.co/spaces) or Inference Endpoints (https://huggingface.co/inference-endpoints)."
}
No generated text found in the response.

### 5. Run the Streamlit App

```bash
# Run the app using Streamlit
streamlit run huggingfacechatbots.py
```

### Explanation:

- **API_URL**: The URL for the model endpoint you want to use. Replace `"gpt2"` with the desired model.
- **API_TOKEN**: Your Hugging Face API token, which you should replace with your own.
- **query() function**: This function sends a POST request to the API endpoint with your input prompt and returns the model's response.

This setup will allow you to interact with Hugging Face's models using their API, enabling you to integrate powerful language models into your Streamlit application. Let me know if you have any further questions!

---

Setting up a virtual environment is a best practice in Python development for several reasons:

### 1. **Dependency Isolation**

- **Avoid Conflicts**: Different projects may require different versions of the same package. If you install packages globally, you could run into version conflicts, where one project requires a version of a package that is incompatible with another project.
- **Self-Contained Environments**: A virtual environment creates a self-contained directory that contains all the dependencies your project needs, ensuring that your project is insulated from changes in other projects.

### 2. **Project Portability**

- **Reproducibility**: By using a virtual environment and a `requirements.txt` file (which lists all your project's dependencies), you can easily share your project with others or deploy it in different environments, and it will work the same way everywhere.
- **Version Control**: You can control and lock down the versions of packages your project uses, making it easier to reproduce the exact environment later on, even if newer versions of the packages are released.

### 3. **Cleaner Global Environment**

- **Keep Global Python Installation Clean**: By using virtual environments, you avoid cluttering your global Python installation with packages that are only needed for specific projects.
- **Easier Maintenance**: You can quickly identify and manage dependencies for each project without worrying about affecting other projects.

### 4. **Security**

- **Minimize Security Risks**: By isolating your project dependencies, you reduce the risk of accidentally introducing vulnerabilities from unrelated packages installed globally.

### 5. **Flexibility in Python Version**

- **Multiple Python Versions**: Virtual environments allow you to use different versions of Python for different projects. For instance, one project might need Python 3.6 while another might require Python 3.9.

### How Virtual Environments Work:

- **Python Executables**: When you create a virtual environment, it copies the Python executable and creates a local environment in the project's directory. This environment uses the copied Python executable to install packages locally within the project.
- **Local `pip`**: The `pip` installer inside the virtual environment only installs packages to the environment's directory, not system-wide.

### Example Workflow:

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```
2. **Activate the environment**:
   ```bash
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. **Install packages**:
   ```bash
   pip install package_name
   ```
4. **Deactivate the environment**:
   ```bash
   deactivate
   ```

In summary, using a virtual environment is a recommended practice for Python projects as it helps ensure that your project remains portable, maintainable, and free from dependency conflicts.

---

The `pip install requests` command is used to install the `requests` library in your Python environment. Here’s why you would install and use the `requests` library:

### 1. **Simplified HTTP Requests**

- The `requests` library is a powerful and user-friendly library for making HTTP requests in Python. It simplifies tasks like sending GET, POST, PUT, DELETE requests, handling query parameters, and managing headers.
- Instead of dealing with the complexities of handling low-level networking and HTTP operations, `requests` provides a high-level interface to interact with web services and APIs.

### 2. **Interacting with Web APIs**

- If your Python application needs to interact with web services or APIs (like RESTful APIs), `requests` is the go-to library. For example, if you want to send data to a server, retrieve information from a REST API, or download content from a website, `requests` makes it straightforward.
- For instance, when interacting with Hugging Face's API or any other online API, `requests` allows you to send HTTP requests and handle the responses with minimal effort.

### 3. **Easy to Use**

- The `requests` library is designed to be very intuitive and easy to use, making it ideal for both beginners and experienced developers. Here’s an example of a simple GET request:

  ```python
  import requests

  response = requests.get('https://api.example.com/data')
  if response.status_code == 200:
      data = response.json()
      print(data)
  ```

- In the above example, `requests.get` is used to send a GET request to a URL, and the response is handled simply.

### 4. **Handling Complex HTTP Operations**

- The `requests` library can handle more complex HTTP operations such as:
  - Sending form data.
  - Handling authentication.
  - Managing sessions and cookies.
  - Uploading files.
  - Handling timeouts and retries.

### 5. **Well-Documented and Widely Used**

- `requests` is one of the most popular Python libraries with extensive documentation and community support. This makes it easier to find examples, troubleshoot issues, and integrate it into your projects.

### Use Case Example:

If you're building a Streamlit app that needs to interact with an external API (like the Hugging Face API), you’d use `requests` to send and receive data:

```python
import requests

url = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer YOUR_API_TOKEN"}

data = {"inputs": "Hello, world!"}
response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    generated_text = response.json()
    print(generated_text)
```

In this example, `requests` is used to send a POST request to a model inference API, handle the response, and then process the returned data.

In summary, you install the `requests` library because it provides a simple and powerful way to interact with web services, making HTTP requests easy to handle in your Python applications.
"# Hugging-Face-Models" 

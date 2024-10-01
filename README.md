
# AI SaaS App

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Get API Key from OpenAI**

   - Visit [OpenAI's website](https://platform.openai.com/account/api-keys) to create or retrieve your API key.

3. **Create a `.env` File**

   - In the root directory of the project, create a `.env` file.

4. **Add the OpenAI API Key to the `.env` File**

   - Inside the `.env` file, add the following line:
     ```bash
     OPENAI_API_KEY="your-openai-api-key-here"
     ```

5. **Install Dependencies**

   - Install the required Python libraries using `pip`:
     ```bash
     pip install openai python-dotenv
     ```

6. **Run the Project**

   - You should now be able to run the project. Make sure the `.env` file is loaded before starting the application.

```bash
python your_script.py
```

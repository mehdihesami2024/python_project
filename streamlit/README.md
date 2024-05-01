## Password Generator Dashboard
the password generator dashboard is an interactive web application built with pyton and streamlit.it can create different of types passwords by number, sequence of wrds or symbole according a user's request.

## Project Structure

the project has the following structure:
1. ` pass_generator.py`:a python mpdule contain password_generators classes `pincode` , `Random_password`, `Memorable_password`.
2. `app.py`: a python script in which we used streamlit to creat web app for passswords generator. 
3. `README.md`: a documentation for the project solution. you are currently reading this.

## Getting started:
follow instructure bellow to set up this project on your local machine.

### prerequisites
python 3.6 or later
streamlit  
NLTK (Natural Language Toolkit)

to install NLTK use :
```bash
pip install nltk
```
after installing nltk you need to download words corpus. run python and type this commands.
```python
import nltk
nltk.download("words")
```
then install streamlit use pip.
```bash 
pip install streamlit
```

You can install all the required dependencies using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```
## Usage

After following the installation steps, you can run the Streamlit web app as follows:

```bash
streamlit run app.py
```

This will open a web page in your default browser running on your localhost.

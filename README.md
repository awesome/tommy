# Tommy
Free opensource modular virtual assistant

*For the moment, Tommy works __only__ on Linux/MacOS systems*

## Requirements

First you need __python3__, __pip3__, and __git__ on your system.

### Linux users

Depending on your distribution and your package manager, run (example for ubuntu):

`
sudo apt-get install libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 python3-tk festival
`

*Package names may vary depending on distributions*

### MacOS users

First run :

`
xcode-select --install
`

Next you need to install a package manager named [brew](http://brew.sh/) and install portaudio:

```
brew remove portaudio
brew install portaudio
```

## Installation


### Develop Branch
Open a terminal and run:

```
git clone https://github.com/amark97/tommy
pip3 install -r tommy/requirements.txt
```

For starting Tommy just do:

`
python3 tommy/tommy-assistant.py
`


### PIP Branch


Install the PyPi Package
```
pip install tommy

```

## PIP Branch

### Commands

```
python3 setup.py develop
python3 setup.py test
```

### `.env` aka "Dot Env"

https://github.com/theskumar/python-dotenv/

Set up tommy `.env` as it's git ignored:

```
cp .env-example .env
```

### Tests

Unit tests using nose:

http://nose.readthedocs.io/en/latest/

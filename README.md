# Respawn Realm

A web-based gaming platform built with Flask and MySQL, providing a seamless interface for game management and user interaction.

## Description

Respawn Realm is a dynamic web application that offers a platform for gaming enthusiasts. The application features a clean interface with dedicated sections for games, menu navigation, and pricing information.

## Technologies Used

- Python 3.12
- Flask 3.0.3
- MySQL
- SQLAlchemy
- HTML/CSS/JavaScript

## Prerequisites

- Python 3.12 or higher
- MySQL Server
- Virtual Environment (recommended)

## Installation

1. Clone the repository
```bash
git clone https://github.com/DarkGuardian641/Respawn-Realm.git
cd Respawn-Realm
```

2. Create and activate a virtual environment
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install required dependencies
```bash
pip install -r requirements.txt
```

4. Configure the database
   - Create a MySQL database
   - Update the database configuration in `instance/formdata.db`

5. Initialize the application
```bash
python main.py
```

## Project Structure

```
RESPAWN REALM/
├── env/                    # Virtual environment
├── Include/               
│   └── site/              # Site-specific files
├── instance/
│   └── formdata.db        # Database file
├── MySQL/
│   └── queries.sql        # SQL queries
├── static/
│   ├── assets/            # Static assets
│   │   ├── Games/
│   │   ├── Icons/
│   │   ├── Menu/
│   │   └── Slider Images/
│   ├── css/
│   │   └── styles.css     # CSS styles
│   └── js/
│       └── scripts.js     # JavaScript files
├── templates/             # HTML templates
│   ├── form.html
│   ├── index.html
│   ├── menu.html
│   ├── play.html
│   └── pricing.html
├── main.py               # Application entry point
├── requirements.txt      # Project dependencies
└── README.md            # This file
```

## Features

- Dynamic game management system
- User-friendly interface
- Responsive design
- Form handling capabilities
- Menu and pricing sections
- Interactive gameplay features

## Usage

After installation, access the application through your web browser:

```
http://localhost:5000
```

Navigate through different sections using the menu:
- Home page: `/`
- Game section: `/play`
- Menu: `/menu`
- Pricing: `/pricing`
- Forms: `/form`

## Configuration

The application uses environment-based configuration. Key configurations can be modified in:
- `pyenv.cfg` for Python environment settings
- Database configurations in the instance folder

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/improvement`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/improvement`)
5. Create a Pull Request

## Support

For support, please open an issue in the GitHub repository.

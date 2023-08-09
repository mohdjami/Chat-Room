# Asynchronous WebSocket Chat Application

This is an asynchronous WebSocket chat application built using the Django framework. The application allows users to send and receive messages in real-time without having to refresh the page.

## Features
- Real-time messaging: Users can send and receive messages instantly without the need to refresh the page.
- Asynchronous communication: The application utilizes Django Channels to handle WebSocket connections and enable asynchronous I/O, ensuring high-concurrency and low-latency communications.
- User-friendly interface: The chat interface is intuitive and easy to use, providing a seamless chatting experience.
- Performance optimization: The application has been optimized for performance by implementing caching using Django's caching framework and minimizing database queries.


## Installation

To set up the application, follow these steps:
1. Clone the repository: `git clone https://github.com/your-username/chat-app.git`
2. Navigate to the project directory: `cd chat-app`
3. Create a virtual environment: `virtualenv env`
5. Activate the virtual environment:
   - For Windows: `env\Scripts\activate`
   - For Unix or Linux: `. env/bin/activate`
6. Install django: `pip install django`
7. Run database migrations: `python manage.py migrate`
8. Start the development server: `python manage.py runserver`

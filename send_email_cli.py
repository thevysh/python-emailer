import sys

try:
    from main import send_plain_email
except Exception as e:
    print("Error: could not import send_plain_email_to from main.py:", e)
    print("Make sure you're running this script from the project root and that main.py is present.")
    sys.exit(1)


def read_multiline(prompt: str) -> str:
    print(prompt)
    print("(Enter message; finish with a single semicolon ';' on its own line)")
    lines = []
    try:
        while True:
            line = input()
            if line == ';':
                break
            lines.append(line)
    except KeyboardInterrupt:
        print('\nInput cancelled by user.')
        sys.exit(1)

    return '\n'.join(lines)


def main():
    try:
        to_addr = input('Receiver email: ').strip()
        if not to_addr:
            print('Receiver email is required.')
            return

        subject = input('Subject: ').strip()
        if not subject:
            subject = '(No subject)'

        body = read_multiline('Message body:')
        if not body:
            print('Warning: message body is empty; sending anyway.')

        print(f"Sending email to {to_addr}...")
        send_plain_email(to_addr, subject, body)

    except Exception as e:
        print('Failed to send email:', e)


if __name__ == '__main__':
    main()

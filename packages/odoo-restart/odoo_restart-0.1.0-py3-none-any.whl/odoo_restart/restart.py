from fabric import Connection

SC_PRIVATE_KEY_PATH = "/opt/id_rsa"
USER = "ubuntu"
RESTART_CMD = "service odoo restart"


def restart_with_private_key(host):
    try:
        with Connection(
            host=host,
            user=USER,
            connect_kwargs=dict(key_filename=[SC_PRIVATE_KEY_PATH]),
        ) as conn:
            restart_result = conn.sudo(RESTART_CMD, hide=True)
            if restart_result:
                result_value = restart_result.stdout.strip()
                print(f"Restart command output: {result_value}")
    except Exception as e:
        print(f"Error: {e}")


def main():
    # Replace 'your_host_ip' with the actual IP address or hostname of the remote host
    host = "localhost"
    restart_with_private_key(host)


if __name__ == "__main__":
    main()

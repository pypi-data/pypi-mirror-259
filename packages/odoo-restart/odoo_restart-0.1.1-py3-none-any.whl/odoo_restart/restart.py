from fabric import Connection
import os


SC_PRIVATE_KEY_PATH = os.environ.get("KZM_PRIVATE_KEY_PATH", "/opt/id_rsa")
USER = os.environ.get("KZM_USER", "ubuntu")
HOST = os.environ.get("KZM_HOST", "localhost")

RESTART_CMD = "service odoo restart"

if __name__ == "__main__":
    try:
        with Connection(
            host=HOST,
            user=USER,
            connect_kwargs=dict(key_filename=[SC_PRIVATE_KEY_PATH]),
        ) as conn:
            restart_result = conn.sudo(RESTART_CMD, hide=True)
            if restart_result:
                result_value = restart_result.stdout.strip()
                print(f"Restart command output: {result_value}")
    except Exception as e:
        print(f"Error: {e}")

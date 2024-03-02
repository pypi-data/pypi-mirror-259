from multiprocessing import Event, Process, Queue

from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ed25519
from rich.live import Live
from rich.spinner import Spinner


def generate_ed25519_key_pair():
    """
    Generate Ed25519 key pair.

    Returns:
        tuple: Public key (bytes), Private key (bytes)
    """
    private_key = ed25519.Ed25519PrivateKey.generate()
    public_key = private_key.public_key()
    return public_key, private_key


def serialize_public_key(key):
    """
    Serialize an Ed25519 public key to bytes.

    Args:
        key: Ed25519 public key object.

    Returns:
        bytes: Serialized key.
    """
    return key.public_bytes(encoding=serialization.Encoding.OpenSSH, format=serialization.PublicFormat.OpenSSH)


def serialize_private_key(key):
    """
    Serialize an Ed25519 private key to bytes.

    Args:
        key: Ed25519 private key object.

    Returns:
        bytes: Serialized key.
    """
    return key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.OpenSSH,
        encryption_algorithm=serialization.NoEncryption(),
    )


def find_public_key_with_suffix(suffix, case_insensitive, result_queue, result_event):
    """
    Generate Ed25519 key pairs until the public key ends with a given suffix.

    Args:
        suffix (bytes): The suffix to search for at the end of the public key.
        result_queue (Queue): Queue to store the result.
        result_event (Event): Event to signal when a result is found.
    """
    while not result_event.is_set():
        public_key, private_key = generate_ed25519_key_pair()
        serialized_public_key = serialize_public_key(public_key)
        serialized_private_key = serialize_private_key(private_key)

        if (case_insensitive and serialized_public_key.lower().endswith(suffix)) or serialized_public_key.endswith(
            suffix
        ):
            result_queue.put((serialized_public_key, serialized_private_key))
            result_event.set()
            return


def find_concurrently(suffix, num_processes, case_insensitive):
    """
    Find public keys concurrently using multiprocessing.

    Args:
        suffix (bytes): The suffix to search for at the end of the public key.
        num_processes (int): Number of processes to use.

    Returns:
        tuple: Public key (bytes), Private key (bytes).
    """
    result_event = Event()
    result_queue = Queue()

    processes = []
    for _ in range(num_processes):
        process = Process(
            target=find_public_key_with_suffix,
            args=(
                suffix,
                case_insensitive,
                result_queue,
                result_event,
            ),
        )
        process.start()
        processes.append(process)

    spinner = Spinner("dots", "Generating key pairs...")
    with Live(spinner, refresh_per_second=10, transient=True):
        result_event.wait()

        for process in processes:
            process.join()

        while not result_queue.empty():
            result = result_queue.get()
            if result:
                return result

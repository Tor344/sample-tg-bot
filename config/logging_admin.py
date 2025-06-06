import logging

loger = logging.getLogger("tor")
loger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("py_logging.log")
file_handler.setLevel(logging.WARNING)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
consol_formatter = logging.Formatter("%(name)s - %(levelname)s - %(message)s")

file_handler.setFormatter(file_formatter)
console_handler.setFormatter(consol_formatter)

loger.addHandler(file_handler)
loger.addHandler(console_handler)

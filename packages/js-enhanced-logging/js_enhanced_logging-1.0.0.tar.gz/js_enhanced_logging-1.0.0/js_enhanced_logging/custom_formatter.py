import re
import logging
import colorama
class CustomFormatter(logging.Formatter):
    COLOR_MAP = {
        'DEBUG': colorama.Back.LIGHTBLUE_EX + colorama.Fore.YELLOW,  # Blue background with white text for DEBUG
        'INFO': colorama.Back.GREEN + colorama.Fore.WHITE,  # Green background with white text for INFO
        'WARNING': colorama.Back.YELLOW + colorama.Fore.WHITE,  # Yellow background with white text for WARNING
        'ERROR': colorama.Back.RED + colorama.Fore.WHITE,  # Red background with white text for ERROR
        'CRITICAL': colorama.Back.RED + colorama.Fore.WHITE + colorama.Style.BRIGHT,  # Bright red background with bright white text for CRITICAL
    }

    HIGHLIGHTS = [
        (r'\b\d+\b', colorama.Fore.GREEN),  # Decimal numbers in green
        (r'\b\d+\.\d+\b', colorama.Fore.CYAN),  # Floats in cyan
        (r'\b(?:19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])\b', colorama.Fore.BLUE),  # Dates in blue
        (r'(?:".*?"|\'.*?\')', colorama.Fore.YELLOW),  # Strings in quotes in yellow
        (r'\bTrue\b', colorama.Fore.GREEN + colorama.Style.BRIGHT),  # True in bold green
        (r'\bFalse\b', colorama.Fore.RED + colorama.Style.BRIGHT),  # False in bold red

    ]

    def format(self, record):
        log_level = record.levelname
        message = super().format(record)

        # Apply log level color to the log level part of the message
        log_level_colored = self.COLOR_MAP.get(log_level, '') + log_level + colorama.Style.RESET_ALL

        # Replace the log level in the message with the colored version
        message = message.replace(log_level, log_level_colored, 1)

        # Apply highlighting to the rest of the message
        for pattern, color in self.HIGHLIGHTS:
            message = re.sub(pattern, lambda m: f"{color}{m.group(0)}{colorama.Style.RESET_ALL}", message)

        return message

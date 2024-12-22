# --------------------------------------------------------------------------
#
# Very basic telegram user-bot to mirror messages from multiple sources to
# multiple destinations.
#
# Author: Aggelos Stamatiou, Dec 2024
#
# This source code is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This software is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this source code. If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------

import sys
from telegram.client import Telegram

# Main function
def main():
    # Initialize proxy
    api_id = int(sys.argv[1])
    api_hash = sys.argv[2]
    phone = sys.argv[3]
    db_pass = sys.argv[4]
    db_path = sys.argv[5]
    dest_groups = sys.argv[6].split(",")
    source_groups = sys.argv[7].split(",")
    tg = Telegram(
        api_id=api_id,
        api_hash=api_hash,
        phone=phone,
        database_encryption_key=db_pass,
        files_directory=db_path,
    )
    tg.login()
    
    # Define mirror commands handler
    def mirror_handler(update):
        if not update['message']['is_outgoing'] and str(update['message']['chat_id']) in source_groups:
            for dest in dest_groups:
                data = {
                    'chat_id': dest,
                    'from_chat_id': update['message']['chat_id'],
                    'message_ids': [update['message']['id']],
                    'send_copy': True,
                }
                call_method_result = tg.call_method(method_name='forwardMessages', params=data, block=True)
                call_method_result.wait()
                if call_method_result.error:
                    print(f'Failed to forward the message to group {dest}: {call_method_result.error_info}')

    # Append handler
    tg.add_message_handler(mirror_handler)

    # Wait for termination
    tg.idle()

if __name__ == '__main__':
    main()

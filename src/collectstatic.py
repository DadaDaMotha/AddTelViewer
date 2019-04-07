# 1. Find the apps with static assets
# 2. Copy content to STATIC ROOT

import settings
import os, subprocess
apps_list = os.listdir(settings.APPS_DIR)

for app in apps_list:
    static_path = os.path.join(settings.APPS_DIR, app, 'static')
    command = f'cp {static_path} {settings.STATIC_ROOT}'

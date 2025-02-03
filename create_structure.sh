#!/bin/bash

# نام پروژه
PROJECT_NAME="ai-azad"

# ایجاد ساختار پروژه
mkdir -p $PROJECT_NAME/{backend,frontend,docs}

# ایجاد ساختار بک‌اند
mkdir -p $PROJECT_NAME/backend/{data,models,services,utils,tests}
touch $PROJECT_NAME/backend/app.py
touch $PROJECT_NAME/backend/data/preprocess_text.py
touch $PROJECT_NAME/backend/models/bert_model.py
touch $PROJECT_NAME/backend/services/search_service.py
touch $PROJECT_NAME/backend/utils/db_utils.py
touch $PROJECT_NAME/backend/tests/test_preprocess_text.py
touch $PROJECT_NAME/backend/Dockerfile
touch $PROJECT_NAME/backend/requirements.txt

# ایجاد ساختار فرانت‌اند
mkdir -p $PROJECT_NAME/frontend/{public,src/components,src/services}
touch $PROJECT_NAME/frontend/public/index.html
touch $PROJECT_NAME/frontend/src/App.js
touch $PROJECT_NAME/frontend/src/components/SearchComponent.js
touch $PROJECT_NAME/frontend/src/services/api.js
touch $PROJECT_NAME/frontend/src/index.js
touch $PROJECT_NAME/frontend/Dockerfile
touch $PROJECT_NAME/frontend/package.json
touch $PROJECT_NAME/frontend/README.md

# ایجاد مستندات و فایل‌های کلی
touch $PROJECT_NAME/docs/index.md
touch $PROJECT_NAME/docker-compose.yml
touch $PROJECT_NAME/README.md
touch $PROJECT_NAME/requirements.txt

# پیام موفقیت
echo "ساختار پروژه $PROJECT_NAME با موفقیت ایجاد شد!"
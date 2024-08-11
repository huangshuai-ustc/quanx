#!/bin/bash

# 检查是否有未提交的更改
if [[ -n $(git status -s) ]]; then
    # 设置提交信息
    commit_message="Auto commit - $(date '+%Y-%m-%d %H:%M:%S')"

    # 添加所有更改
    git add .

    # 提交更改
    git commit -m "$commit_message"

    # 推送到远程仓库
    git push origin main

    echo "Changes have been pushed."
else
    echo "No changes to commit."
fi

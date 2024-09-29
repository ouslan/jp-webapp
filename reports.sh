#!/bin/bash

# Define output file
OUTPUT_FILE="git_contributors_report.txt"

# Set the date for one week ago
export _GIT_SINCE=$(date -d '1 week ago' '+%Y-%m-%d')

# Clear output file
echo "" >"$OUTPUT_FILE"

# Function to check for commits in a branch
has_commits() {
  local branch="$1"
  git rev-list --count --since="$_GIT_SINCE" "$branch" | grep -q '[1-9]'
}

# Function to generate reports for a specific branch
generate_report_for_branch() {
  local branch="$1"

  if ! has_commits "$branch"; then
    return # Skip if no commits
  fi

  {
    echo "=== Detailed Git Stats for Branch: $branch ==="
    git checkout "$branch" &>/dev/null
    git-quick-stats -T
    git-quick-stats -c

    # Only for the main branch
    if [[ "$branch" == "main" ]]; then
      echo ""
      git-quick-stats -b
    fi

    echo "------------------------------------------"
  } >>"$OUTPUT_FILE"
}

# Get all branches and loop through each
git fetch --all
branches=$(git branch -r | grep -v '\->') # List remote branches, excluding HEAD

# Generate report for the main branch first
generate_report_for_branch "main"

# Loop through the remaining branches
for branch in $branches; do
  # Strip the 'origin/' prefix
  branch_name=${branch#origin/}

  # Skip the main branch if already processed
  if [[ "$branch_name" != "main" ]]; then
    generate_report_for_branch "$branch_name"
  fi
done

# Check if the command succeeded
if [[ $? -eq 0 ]]; then
  echo "Report generated successfully: $OUTPUT_FILE"
else
  echo "Failed to generate the report."
fi

# Checkout back to the main branch
git checkout main &>/dev/null

# GitHub Stats Generator 🚀

A private GitHub Action that generates accurate GitHub statistics, including data from private repositories and collaborations. This tool automatically updates your GitHub profile README with detailed stats about your GitHub activity.

## 🌟 Features

- Accurate commit counts (including private repos)
- Total stars across all repositories
- PR and Issue statistics
- Language distribution
- Daily automatic updates
- Private repository support
- Clean, emoji-rich display

## 📋 Prerequisites

1. GitHub account
2. A repository named exactly as your GitHub username (for profile README)
3. Basic knowledge of GitHub Actions

## 🔧 Setup Instructions

### 1. Profile Repository Setup

1. Create a repository named exactly as your GitHub username if you haven't already
2. Make sure it's public (required for GitHub profile README)
3. Add these markers in your profile README.md where you want the stats to appear:
   ```markdown
   <!-- START_SECTION:github_stats -->
   <!-- END_SECTION:github_stats -->
   ```

### 2. Stats Generator Repository Setup

1. Create a new private repository for this stats generator
2. Clone this repository:
   ```bash
   git clone https://github.com/harshsingh-io/harshsingh-io.git
   cd harshsingh-io
   ```
3. Copy all the project files maintaining this structure:
   ```
   .
   ├── .github/
   │   └── workflows/
   │       └── update-stats.yml
   ├── src/
   │   ├── __init__.py
   │   ├── github_stats.py
   │   ├── readme_generator.py
   │   └── update_stats.py
   ├── templates/
   │   └── stats.md.j2
   ├── .gitignore
   ├── README.md
   └── requirements.txt
   ```

### 3. Generate GitHub Personal Access Token (PAT)

1. Go to GitHub Settings → Developer settings → Personal access tokens → Tokens (classic)
2. Click "Generate new token (classic)"
3. Name: `GitHub Stats Generator`
4. Select scopes:
   - `repo` (full access)
   - `read:user`
   - `user:email`
5. Copy the generated token

### 4. Configure Repositories

1. In your profile repository (username/username):
   - Go to Settings → Secrets and variables → Actions
   - Add new repository secret:
     - Name: `GH_PAT`
     - Value: Your generated PAT

2. In the workflow file (`.github/workflows/update-stats.yml`):
   - Replace `your-username` with your GitHub username:
     ```yaml
     - uses: actions/checkout@v2
       with:
         repository: your-username/your-username
         token: ${{ secrets.GH_PAT }}
     ```

## 🚀 Usage

The stats will automatically update daily at midnight UTC. To manually trigger an update:

1. Go to the "Actions" tab in your profile repository
2. Select "Update GitHub Stats" workflow
3. Click "Run workflow"

## 🔍 Local Testing

1. Clone your stats generator repository
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file with your PAT:
   ```
   GITHUB_TOKEN=your_pat_here
   ```
5. Run the script:
   ```bash
   python -m src.update_stats
   ```

## 🔒 Security Notes

- Keep the stats generator repository private
- Never commit the `.env` file
- Regularly rotate your PAT
- Don't share your PAT with anyone

## 🐛 Troubleshooting

1. **Stats not updating?**
   - Check if GitHub Actions is enabled
   - Verify the PAT has correct permissions
   - Check Actions logs for errors

2. **Missing private repo data?**
   - Ensure PAT has `repo` scope
   - Verify PAT hasn't expired

3. **Action failing?**
   - Check if PAT is correctly set in secrets
   - Verify repository names and paths

## 📝 License

MIT

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 💖 Credits

Created by [Harsh Singh](https://github.com/harshsingh-io)
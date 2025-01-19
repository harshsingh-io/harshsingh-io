from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import re
from typing import Dict, Any

class ReadmeGenerator:
    def __init__(self, template_dir: str = "templates"):
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template("stats.md.j2")
        
    def generate_stats_section(self, stats: Dict[str, Any]) -> str:
        """Generate the stats section using the template."""
        return self.template.render(stats=stats)

    def update_readme(self, readme_path: str, stats_section: str) -> bool:
        """
        Update the README file with new stats.
        Returns True if the content changed.
        """
        readme = Path(readme_path)
        if not readme.exists():
            raise FileNotFoundError(f"README file not found at {readme_path}")

        content = readme.read_text()
        
        # Define markers for the stats section
        start_marker = "<!-- START_SECTION:github_stats -->"
        end_marker = "<!-- END_SECTION:github_stats -->"
        
        # Create the pattern to match the section
        pattern = f"({start_marker}).*({end_marker})"
        replacement = f"{start_marker}\n{stats_section}\n{end_marker}"
        
        new_content = re.sub(
            pattern,
            replacement,
            content,
            flags=re.DOTALL
        )
        
        if new_content != content:
            readme.write_text(new_content)
            return True
            
        return False 
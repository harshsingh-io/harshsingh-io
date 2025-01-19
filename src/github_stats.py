from datetime import datetime, timezone
import os
from typing import Dict, Any
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

class GitHubStats:
    def __init__(self, token: str):
        self.token = token
        self.client = self._create_client()

    def _create_client(self) -> Client:
        """Create an authenticated GraphQL client."""
        transport = RequestsHTTPTransport(
            url='https://api.github.com/graphql',
            headers={'Authorization': f'Bearer {self.token}'}
        )
        return Client(transport=transport, fetch_schema_from_transport=True)

    def fetch_user_stats(self) -> Dict[str, Any]:
        """Fetch comprehensive GitHub statistics for the authenticated user."""
        query = gql("""
        query {
          viewer {
            login
            name
            contributionsCollection {
              totalCommitContributions
              restrictedContributionsCount
            }
            repositories(first: 100, ownerAffiliations: [OWNER, COLLABORATOR, ORGANIZATION_MEMBER]) {
              totalCount
              nodes {
                nameWithOwner
                stargazerCount
                primaryLanguage {
                  name
                }
                issues(states: OPEN) {
                  totalCount
                }
                pullRequests(states: OPEN) {
                  totalCount
                }
              }
            }
            pullRequests(first: 1, orderBy: {field: CREATED_AT, direction: DESC}) {
              totalCount
            }
            issues(first: 1, orderBy: {field: CREATED_AT, direction: DESC}) {
              totalCount
            }
          }
        }
        """)

        result = self.client.execute(query)
        return self._process_stats(result)

    def _process_stats(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """Process the raw GraphQL response into useful statistics."""
        viewer = data['viewer']
        repos = viewer['repositories']['nodes']

        total_stars = sum(repo['stargazerCount'] for repo in repos)
        languages = {}
        for repo in repos:
            if repo['primaryLanguage']:
                lang = repo['primaryLanguage']['name']
                languages[lang] = languages.get(lang, 0) + 1

        return {
            'username': viewer['login'],
            'name': viewer['name'],
            'total_commits': (
                viewer['contributionsCollection']['totalCommitContributions'] +
                viewer['contributionsCollection']['restrictedContributionsCount']
            ),
            'total_repos': viewer['repositories']['totalCount'],
            'total_stars': total_stars,
            'total_prs': viewer['pullRequests']['totalCount'],
            'total_issues': viewer['issues']['totalCount'],
            'languages': dict(sorted(languages.items(), key=lambda x: x[1], reverse=True)),
            'last_updated': datetime.now(timezone.utc).isoformat()
        } 
function copyLeaderboardLink() {
    const url = window.location.origin + window.location.pathname + '#leaderboard';
    navigator.clipboard.writeText(url);
  }
  
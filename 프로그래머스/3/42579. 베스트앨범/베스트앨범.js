function solution(genres, plays) {
    var answer = [];
    const genreMap = new Map(); 
    
    
    for (let i = 0; i < genres.length; i++) {
        if (!genreMap.has(genres[i])) {
            genreMap.set(genres[i], { total: 0, songs: [] });
        }
        
        const genre = genreMap.get(genres[i]);
        genre.total += plays[i];
        genre.songs.push({ id: i, playCount: plays[i] });
    }
    
    const sortedGenres = [...genreMap.entries()].sort((a, b) => b[1].total - a[1].total);
    
    for (const [genre, info] of sortedGenres) {
        const sortedSongs = info.songs.sort((a, b) => {
            if (b.playCount === a.playCount) return a.id - b.id;
            return b.playCount - a.playCount;
        });
        
        for (let i = 0; i < Math.min(2, sortedSongs.length); i++) {
            answer.push(sortedSongs[i].id);
        }
    }
    
    return answer;
}
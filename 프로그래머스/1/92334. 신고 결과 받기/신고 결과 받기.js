function solution(id_list, report, k) {    
    const reports = new Set(report);
    const reportCount = new Map();
    const mailCount = new Map();
    
    id_list.forEach(id => {
        reportCount.set(id, 0);
        mailCount.set(id, 0);
    });
    
    reports.forEach(entry => {
        const [reporter, reported] = entry.split(' ');
        reportCount.set(reported, reportCount.get(reported) + 1);
    });
    
    const blockUsers = new Set(
        [...reportCount.entries()]
            .filter(([_, count]) => count >= k)
            .map(([id]) => id)
    );
    
    reports.forEach(entry => {
        const [reporter, reported] = entry.split(' ');
        if (blockUsers.has(reported)) {
            mailCount.set(reporter, mailCount.get(reporter) + 1);
        }
    });
    
    return id_list.map(id => mailCount.get(id));
}
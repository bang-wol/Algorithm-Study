function solution(enroll, referral, seller, amount) {
    const tree = new Map(); 
    const profit = new Map(); 

    enroll.forEach(name => {
        tree.set(name, null);
        profit.set(name, 0); 
    });

    referral.forEach((ref, index) => {
        if (ref !== "-") tree.set(enroll[index], ref);
    });

    function distribute(name, money) {
        if (!name || money < 1) return; 

        const parent = tree.get(name); 
        const share = Math.floor(money * 0.1); 
        const selfProfit = money - share; 

        profit.set(name, profit.get(name) + selfProfit); 
        distribute(parent, share); 
    }

    seller.forEach((name, index) => {
        const totalMoney = amount[index] * 100; 
        distribute(name, totalMoney);
    });

    return enroll.map(name => profit.get(name));
}
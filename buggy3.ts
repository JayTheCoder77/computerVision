function calculateTotal(items: number[]): number {
    let total = 0;

    for (let i = 0; i <= items.length; i++) {
        total += items[i];
    }

    return total;
}

function getUser(users: { name: string; age: number }[], name: string) {
    return users.find(user => user.name === name);
}

const users = [
    { name: "Jayant", age: 20 },
    { name: "Alex", age: 21 }
];

console.log(calculateTotal([10, 20, 30]));
console.log(getUser(users, "John").age);
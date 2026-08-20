fn divide(a: i32, b: i32) -> i32 {
    a / b
}

fn find_user(users: Vec<(&str, i32)>, name: &str) -> i32 {
    for (user, age) in users {
        if user == name {
            return age;
        }
    }

    panic!("User not found");
}

fn main() {
    let users = vec![
        ("Jayant", 20),
        ("Alex", 21),
    ];

    println!("{}", divide(10, 0));
    println!("{}", find_user(users, "John DOE"));
}
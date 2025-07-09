//This project will have extra fluff to have
//extra things in one place for practice
use std::io;

fn main() {
   println!("Day Two pt2 test driver:");
   println!("Type something and hit enter");
   
   let mut guess = String::new();
   
   io::stdin()
      .read_line(&mut guess)
      .expect("Failed to read line");
   
   println!("You guessed: {}", guess);
   
   //Casting a string to int
   //Since the var has the same name, we're shadowing the var into
   //an int
   //trim eliminates whitespace at the beginning and end
   //i.e. removing \n
   // parse casts the var and : u32 annotates it as a 32 bit unsigned integer
   // parse refuses to cast non numerical characters
   // Parse also returns Result which is an enum type that tells you
   // whether it failed or not
   let guess: u32 = guess.trim()
      .parse()
      .expect("Please type a number");
   
}

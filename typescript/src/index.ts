type Info = {
  name: string;
  age: number;
}

const input: Info[] = [
  {name: 'Andrew D. Huberman', age: 48},
  {name: 'Marco Rubio', age: 52},
  {name: 'Lindsey Graham', age: 68},
  {name: 'Ted Cruz', age: 52},
  {name: 'Brian Tracy', age: 79},
  {name: 'Jim Rohn', age: 79},
  {name: 'Donald Trump', age: 77},
  {name: 'Russell Westbrook', age: 34},
  {name: "Luka Dončić", age: 25},
  {name: 'LeBron James', age: 38},
  {name: 'Chris Paul', age: 38},
  {name: 'Kevin Durant', age: 34},
  {name: 'Jayson Tatum', age: 25},
  {name: 'P. J. Tucker', age: 38},
  {name: "De'Anthony Melton", age: 25},
  {name: "Jalen McDaniels", age: 25},
]

function main() {
  const results:Record<number, string[]> = {};
  input.map((item: Info) => {
    if (!results[item.age]) {
      results[item.age] = [];
    }
    results[item.age].push(item.name);
  });
  console.table(results)
}


main();

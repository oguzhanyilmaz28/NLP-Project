let x = 42;
let y = 28;
let z = 7;
let v = 99;
let enbuyuk = x;
let enkucuk = x;

if (y > enbuyuk) {
    enbuyuk = y;
} else if (y < enkucuk) {
    enkucuk = y;
}

if (z > enbuyuk) {
    enbuyuk = z;
} else if (z < enkucuk) {
    enkucuk = z;
}

if (v > enbuyuk) {
    enbuyuk = v;
} else if (v < enkucuk) {
    enkucuk = v;
}

console.log("en büyük sayi:"+enbuyuk);
console.log("en büyük sayi:"+enkucuk);


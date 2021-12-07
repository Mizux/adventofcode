#!/usr/bin/env node
//require('./input.js');
import {INPUT} from './input.js';

const yourCleverSolution = (input) => {
  //input = "16,1,2,0,4,2,7,1,2,14";
  const crabs = input.split(",");
  const max = crabs.reduce((acc, v) => (v > acc ? v : acc), 0);
  const resultat = { pos: 0, fuel: Infinity };
  for (let i = 1; i <= max; i++) {
    const currentPosFuel = crabs.reduce((fuel, pos) => fuel + Math.abs(pos -i), 0);
    if (currentPosFuel < resultat.fuel) {
      resultat.fuel = currentPosFuel;
      resultat.pos = i;
    }
  }
  console.log(resultat);
  return resultat.pos;
};

yourCleverSolution(INPUT)

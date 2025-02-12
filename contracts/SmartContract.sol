// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract SmartContract {
    address public owner;
    uint public balance;
    
    event ExecutedTransaction(address indexed sender, uint amount);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    constructor() {
        owner = msg.sender;
        balance = 0;
    }

    function deposit() public payable {
        balance += msg.value;
    }

    function withdraw(uint amount) public onlyOwner {
        require(amount <= balance, "Insufficient balance");
        payable(owner).transfer(amount);
        balance -= amount;
    }
}

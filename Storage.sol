pragma solidity ^0.8.0;

contract Storage {
    struct Person {
        string name;
        uint256 age;
        bool isValue;
    }
    Person[] public people;
    mapping (address => bool) public ownerList;
    mapping (string => Person) public peopleMap;

    modifier onlyOwners {
        require(ownerList[msg.sender] == true);
        _;
    }

    constructor() public {
        // Automatically add the contract creator as an owner
        ownerList[msg.sender] = true;
    }

    function addToPeopleList(string memory _name, uint256 _age) public {
        people.push(Person(_name, _age, true));
    }

    function addToPeopleMap(string memory _name, uint256 _age) public onlyOwners {
        assert(!peopleMap[_name].isValue); //will revert if person already exists
        peopleMap[_name] = Person(_name, _age, true);
    }

    function getFromPeopleMap(string memory _name) public view returns (string memory, uint256) {
        if(!peopleMap[_name].isValue) {
            return ("none", 0);
        }
        return (peopleMap[_name].name, peopleMap[_name].age);
    }

    function removePersonFromMap(string memory _name) public onlyOwners {
        //peopleMap[_name].isValue = false;
        delete peopleMap[_name];
    }

}
import React, {Component} from "react";
import {render} from "react-dom";
import Homepage from "./HomePage";

export default class App extends Component{
    constructor(props){
        super(props);
        this.state={
            
        }
        
    }
    render(){
        return(<div>
            <Homepage />
           

        </div>);

//  return <h1>{this.props.name}</h1>;

    }
}

const appDiv=document.getElementById("app");
render(<App />,appDiv);
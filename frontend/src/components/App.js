import React, {Component} from "react";
import {render} from "react-dom";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


export default class App extends Component{
    constructor(props){
        super(props);
        this.state={
            
        }
        
    }
    render(){
        return(<div>
           
          <h1>Helloworld</h1>

        </div>);

//  return <h1>{this.props.name}</h1>;

    }
}

const appDiv=document.getElementById("app");
render(<App />,appDiv);
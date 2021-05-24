import React, {Component} from "react";
import SelectModelPage from "./SelectModelPage";
import {
    BrowserRouter as Router,
    Switch,
    Link,
    Redirect,
    Route
} from "react-router-dom";

export default class Homepage extends Component{
    constructor(props){
        super(props);

    }
    // exact is vv important
    render(){
        return <Router>
            <Switch>
                <Route exact path='/'><p>THis is the home page</p></Route>
                <Route path = '/Select_Model' component={SelectModelPage}/>
            </Switch>
        </Router>;

    }
}
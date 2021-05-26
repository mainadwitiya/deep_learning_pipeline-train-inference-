import React, { Component } from "react";
import ModelPage from "./ModelPage";
import SelectModel from "./SelectModel";
import {
  BrowserRouter as Router,
  Switch,
  Link,
  Redirect,
  Route,
} from "react-router-dom";

export default class Routes extends Component {
  constructor(props) {
    super(props);
  }
  // exact is vv important
  render() {
    return (
      <Router>
        <Switch>
          <Route exact path="/" component={SelectModel} />
          <Route exact path="/model/tensorflow" component={ModelPage} />
        </Switch>
      </Router>
    );
  }
}

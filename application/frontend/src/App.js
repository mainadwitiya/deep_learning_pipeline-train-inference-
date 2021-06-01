import { Route, Switch } from "react-router-dom";

import "./App.css";
import Layout from "./components/layout/Layout";
import HomePage from "./pages/HomePage";
import ModelPage from "./pages/ModelPage";

const App = () => {
  return (
    <Layout>
      <Switch>
        <Route path="/" exact>
          <HomePage />
        </Route>
        <Route path="/model">
          <ModelPage />
        </Route>
      </Switch>
    </Layout>
  );
};

export default App;

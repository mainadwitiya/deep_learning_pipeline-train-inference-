import { Route, Switch } from "react-router-dom";

import "./App.css";
import Layout from "./components/layout/Layout";
import HomePage from "./pages/HomePage";
import ModelPage from "./pages/ModelPage";
import FileEditor from "./pages/RichTextEditor";

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
        <Route path="/tf_config_file_edited">
          <FileEditor />
        </Route>
      </Switch>
    </Layout>
  );
};

export default App;

import axios from "axios";
import { useEffect, useState } from "react";
import API from "../components/utils/API";

const Editor = (props) => {
  const [data, setData] = useState("");

  useEffect(() => {
    const response = axios({
      url: `${API}/file/:filename`,
    });
    const data = response.data;
    setData(data);
  }, []);

  return <div>{data}</div>;
};

export default Editor;

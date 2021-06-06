import React from "react";
import ReactDOM from "react-dom";
import { ContentState, convertToRaw, Editor, EditorState } from "draft-js";
import file from "./hello.txt";

const FileEditor = (props) => {
  let _contentState = ContentState.createFromText(file);
  const raw = convertToRaw(_contentState);
  const [contentState, setContentState] = React.useState(raw);

  const [editorState, setEditorState] = React.useState(
    EditorState.createWithContent()
  );

  const editor = React.useRef(null);

  function focusEditor() {
    editor.current.focus();
  }

  React.useEffect(() => {
    focusEditor();
  }, []);

  return (
    <div className="container mt-4">
      <h4 className="mb-4">Config File</h4>
      <div onClick={focusEditor}>
        <Editor
          ref={editor}
          // editorState={editorState}
          defaultContentState={contentState}
          onContentStateChange={setContentState}
          onChange={(editorState) => setEditorState(editorState)}
        />
      </div>
    </div>
  );
};

export default FileEditor;

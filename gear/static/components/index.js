import React from 'react';
import ReactDOM from 'react-dom';

class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = {

    };
  }

  render() {
    return (
      <div>
        <h1>Test</h1>
      </div>
    )
  }
}

const element = <App />;

ReactDOM.render(element, document.getElementById('app'));
class FighterClass extends React.Componnent {
	render() {
  	return <li>Attack with Sword</li>;
  }
}

class CharClass extends React.Component {
  constructor(props) {
    super(props)
    this.state = {
    	items: [
      	{ text: "Str: ", attr: 19 },
        { text: "Int", attr: 12 },
        { text: "Hp", attr: 46 },
        { text: "AC", attr: 23 }
      ]
    }
  }
  
  render() {
    return (
      <div>
        <h2>Todos:</h2>
        <ol>
        {this.state.items.map(item => (
          <li key={item.id}>
            <label>
              <span className={item.done ? "done" : ""}>{item.text}: {item.attr}</span>
            </label>
          </li>
        ))}
	<CharClass />
        </ol>
      </div>
    )
  }
}

ReactDOM.render(<CharClass />, document.querySelector("#app"))

var React = window.React;
var ReactDOM = window.ReactDOM;
var ReactRouter = window.ReactRouter;
var History = window.History;

var Router = ReactRouter.Router;
var Route = ReactRouter.Route;
var Link = ReactRouter.Link;
var Redirect = ReactRouter.Redirect;
var IndexRoute = ReactRouter.IndexRoute;
var createHistory = History.createHistory;
var useBasename = History.useBasename;


var App = React.createClass({
	loadDB: function(){
		$.ajax({
			url: "scripts/db.json",
			dataType: "json",
			cache: false,
			success: function(data){
				console.debug("db loaded:", data);
				this.setState({data: data});
			}.bind(this),
			error: function(xhr, status, err){
				console.error(status, err.toString());
			}.bind(this)
		});
	},
	getInitialState: function(){
		return {data: {}};
	},
	componentDidMount: function(){
		this.loadDB();
	},
	render: function(){
		var pathname = this.props.location.pathname;
		console.debug(pathname);
		return (
			<div className="app">
				<Header />
				{React.cloneElement(this.props.children || <div/>, { key: pathname })}
				<Footer />
			</div>
		);
	}
});

var Exams = React.createClass({
	render: function(){
		return (
			<div>
				<ul>
					<li><Link to="/exam/a">A级测试</Link></li>
					<li><Link to="/exam/b">B级测试</Link></li>
					<li><Link to="/exam/c">C级测试</Link></li>
				</ul>
			</div>
		);
	}
});

var Exam = React.createClass({
	clickHandler: function(e){
		console.log("clicked");
	},
	render: function(){
		var _t = this.props.params.type;
		return (
			<div className="exam">
				<div className="question">question {_t}</div>
				<ul className="answers">answers</ul>
				<button onClick={this.clickHandler}>submit</button>
			</div>
		);
	}
});

var Home = React.createClass({
	render: function(){
		return (
			<div className="home">
				<p>welcome!</p>
				<p>A => 30/370</p>
				<p>A => 50/694</p>
				<p>A => 80/1071</p>
			</div>
		);
	}
});

var Navs = React.createClass({
	render: function(){
		return (
			<div className="navs">
				<ul>
					<li><Link activeClassName="active" to="/home">Home</Link></li>
					<li><Link activeClassName="active" to="/exams">Exams</Link></li>
				</ul>
			</div>
		);
	}
});


var Header = React.createClass({
	render: function(){
		return (
			<div className="header">
				<h1>CRAC EXAM</h1>
				<Navs />
			</div>
		);
	}
});

var Footer = React.createClass({
	render: function(){
		return (
			<div className="footer">&copy; 2016</div>
		);
	}
});

React.render((
  <Router>
    <Route path="/" component={App}>
      <IndexRoute component={Home}/>
      <Route path="/home" component={Home} />
      <Route path="/exams" component={Exams} />
      <Redirect from="/exam" to="/exam/a"/>
      <Route path="/exam/:type" component={Exam} />
    </Route>
  </Router>
), document.getElementById('app'));
import React,{ Component } from 'react'

class Form extends Component{
constructor(props){
	super(props)
	this.state = { neighbourhood_group:'',neighbourhood:'', latitude:'', longitude:'',room_type:'',minimum_nights:'',number_of_reviews:'',reviews_per_month:'',calculated_host_listings_count:'',availability_365:'', predictedValue: ''}
	this.handleChange = this.handleChange.bind(this)
	//this.handleSubmit = this.handleSubmit.bind(this)
  this.submit = this.submit.bind(this)
}
 

// Form submitting logic, prevent default page refresh
handleSubmit(event){
	const { neighbourhood_group, neighbourhood, latitude, longitude, room_type,minimum_nights, number_of_reviews,reviews_per_month, calculated_host_listings_count, availability_365 } = this.state
	event.preventDefault()
	alert(`
	___Input Variables___\n
	neighbourhood_group : ${neighbourhood_group}
	neighbourhood : ${neighbourhood}
	latitude : ${latitude}
	longitude : ${longitude}
	room_type : ${room_type}
  minimum_nights : ${minimum_nights}
	number_of_reviews : ${number_of_reviews}
  reviews_per_month : ${reviews_per_month}
	calculated_host_listings_count : ${calculated_host_listings_count}
  availability_365: ${availability_365}
	`)
}

// Method causes to store all the values of the
// input field in react state single method handle
// input changes of all the input field using ES6
// javascript feature computed property names
handleChange(event){
  console.log('eventvalue', event.target.value)
  console.log('eventname', event.target.name)
	this.setState({
	[event.target.name] : event.target.value
	})
}

submit(event){
  event.preventDefault()

  const context = this;
fetch("/airpredict", { 
	
	// Adding method type
	method: "POST", 
	
	body: JSON.stringify({
    neighbourhood_group:context.state.neighbourhood_group,
    neighbourhood:context.state.neighbourhood,                   
    latitude:context.state.latitude,
    longitude:context.state.longitude,
    room_type:context.state.room_type, 
    minimum_nights:context.state.minimum_nights, 
    number_of_reviews:context.state.number_of_reviews, 
    reviews_per_month:context.state.reviews_per_month,
    calculated_host_listings_count:context.state.calculated_host_listings_count,
    availability_365:context.state.availability_365
	}),

	// Adding headers to the request
	headers: {
		"Content-type": "application/json; charset=UTF-8"
	}
}) 

// Converting to JSON

  .then(async response => {
    let resp = await response.json()
  //alert(JSON.stringify(resp['result']))
  context.setState({ predictedValue: resp.result });
})
}

render(){
	return(
	<form onSubmit={this.submit}>
		<div>
		<label htmlFor='neighbourhood_group'>neighbourhood_group</label>
		<input
			name='neighbourhood_group'
			placeholder='neighbourhood_group'
			value = {this.state.neighbourhood_group}
			onChange={this.handleChange}
		/>
		</div>
		<div>
		<label htmlFor='neighbourhood'>neighbourhood</label>
		<input
			name='neighbourhood'
			placeholder='neighbourhood'
			value={this.state.neighbourhood}
			onChange={this.handleChange}
		/>
		</div>
		<div>
		<label htmlFor='latitude'>latitude</label>
		<input
			name='latitude'
			placeholder='latitude'
			value={this.state.latitude}
			onChange={this.handleChange}
		/>
		</div>
		<div>
		<label htmlFor='longitude'>longitude</label> 
		<input
			name='longitude'
			placeholder='longitude'
			value={this.state.longitude}
			onChange={this.handleChange}
		/>
		</div>
		<div>
		<label htmlFor='room_type'>room_type</label>
		<input
			name='room_type'
			placeholder='room_type'
			value={this.state.room_type}
			onChange={this.handleChange}
		/>
		</div>
		<div>
		<label htmlFor='minimum_nights'>minimum_nights</label>
		<input
			name='minimum_nights'
			placeholder='minimum_nights'
			value={this.state.minimum_nights}
			onChange={this.handleChange}
		/>
    </div>
		<div>
		<label htmlFor='number_of_reviews'>number_of_reviews</label>
		<input
			name='number_of_reviews'
			placeholder='number_of_reviews'
			value={this.state.number_of_reviews}
			onChange={this.handleChange}
		/>
    </div>
		<div>
		<label htmlFor='reviews_per_month'>reviews_per_month</label>
		<input
			name='reviews_per_month'
			placeholder='reviews_per_month'
			value={this.state.reviews_per_month}
			onChange={this.handleChange}
		/>
    </div>
		<div>
		<label htmlFor='calculated_host_listings_count'>calculated_host_listings_count</label>
		<input
			name='calculated_host_listings_count'
			placeholder='calculated_host_listings_count'
			value={this.state.calculated_host_listings_count}
			onChange={this.handleChange}
		/>
    </div>
    <div>
		<label htmlFor='availability_365'>availability_365</label>
		<input
			name='availability_365'
			placeholder='availability_365'
			value={this.state.availability_365}
			onChange={this.handleChange}
		/>
		<div>
		<button onClick={this.submit}>Save</button>
		</div>
    <div>
      <p className="predicted-value">Predicted price: {String(this.state.predictedValue).replace("[","").replace("]","")}</p>
    </div>
    </div> 
	</form>
	)
}
}
export default Form 
---
title: Proposal for Standardizing the Recording Rendered Targets
status: proposed
latest: true
version-of: warc-rendered-targets
version: 1.0
---
International Internet Preservation Consortium<br/>
Harvesting Working Group

The modifications described below are based on [HTTP Archive 1.2](http://www.google.com/url?q=http%3A%2F%2Fwww.softwareishard.com%2Fblog%2Fhar-12-spec%2F&sa=D&sntz=1&usg=AFQjCNESSsDv3ZkYTVkyfGPjRKpwSlr6AQ)

### \<pages\>

This object represents list of exported pages.

	"pages": [
	    {
	        "startedDateTime": "2009-04-16T12:07:25.123+01:00",
	        "id": "page\_0",
	        "title": "Test Page",
	        "pageTimings": {...},
	        "comment": "",
	        "renderedContent": {...},
	        "renderedElements": [],
	        "map": []
	    }
	]

startedDateTime [string]
: Date and time stamp for the beginning of the page load (ISO 8601 - YYYY-MM-DDThh:mm:ss.sTZD, e.g. 2009-07-24T19:20:30.45+01:00).

id [string]
: Unique identifier of a page within the \<log\>. Entries use it to refer the parent page.

title [string]
: Page title.

pageTimings[object]
: Detailed timing info about page load.

comment [string, optional] (new in 1.2)
: A comment provided by the user or the application.

renderedContent [object]
: Representation of the page's DOM.

renderedElements [array, optional]
: List of images rendered from the final page.

map [array, optional]
: List of clickable areas in the final page.


### \<renderedContent\>

This object represents the DOM of the final page.

	"renderedContent": {
	    "text": "PCFET0NUWVBFIGh0bWw+P...",
	    "encoding": "base64"
	}

text [string]
: HTML of the final page, following any DOM changes during page-load.

encoding [string, optional]
: Encoding used for response text field e.g "base64".


### \<renderedElements\>

This object represents a list of images rendered from the page or some subsection thereof.

	"renderedElements": [
	  {
	    "selector": ":root",
	    "format": "PNG",
	    "content": "iVBORw0KGgoAAAANSU...",
	    "encoding": "base64"
	  }
	]

selector [string]
: The CSS3 selector of an element within the page forming the basis of the image.

format [string]
: The format of the image (e.g. "PNG", "JPEG").

content [string]
: Textual representation of the image content.

encoding [string]
: Encoding used for the content string (e.g. "base64").


### \<map\>

The object represents a list of clickable areas within the page.

	"map": [
	  {
	    "href": "/",
	    "location": {...}
	  }
	]

href [string, optional]
: URL (absolute or relative) of the page to which a click would direct the session.

onClick [string, optional]
: Action from which an onClick event would result. Either a URL (absolute or relative) or a Javascript fragment.

location [object]
: Representation of the area's position and dimensions.


### \<location\>

This object represents a specific area within a page.

	"location": {
	    "bottom": 46,
	    "height": 46,
	    "left": 37,
	    "right": 110,
	    "top": 0,
	    "width": 73
	}

bottom [number]
: Y-coordinate, relative to the viewport origin, of the bottom of the rectangle box.

height [number]
: Height of the rectangle box (This is identical to bottom minus top).

left [number]
: X-coordinate, relative to the viewport origin, of the left of the rectangle box.

right [number]
: X-coordinate, relative to the viewport origin, of the right of the rectangle box.

top [number]
: Y-coordinate, relative to the viewport origin, of the top of the rectangle box.

width [number]
: Width of the rectangle box (This is identical to right minus left).



# Content-Collapse

A tiny jQuery plugin for collapsing your things. 

## Requirements 

* [jQuery](http://jquery.com/)

## HTML structure

```html
<div class="content-accordion">
	<a data-toggle>Content Header</a>
	<div class="content">
		<p>Content goes here.</p>
	</div>
</div>
```

## CSS

```css
.content-collapse{
  border:1px solid #ddd;
  border-radius:5px;
  margin-top:15px;
}
.content-collapse [data-toggle]{
  display:block;
  padding:20px;
  cursor:pointer;

  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.content-collapse .content{
  display:none;
  border-top:1px solid #ddd;
  padding:10px 20px;
}
.content-collapse .open{
  display:block;
}
```

## Getting started

* `git clone` into project or download as .zip and copy files into your project.
* Link script and stylesheet in the head.

```html
<link type="text/css" rel="stylesheet" href="path/to/contentCollapse.css" />
<script type="text/javascript" src="path/to/contentCollapse.js"></script>
```

* Call init method when the DOM is ready.

```javascript
contentCollapse.init();
```

* Start collapsing things.
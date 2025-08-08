# Use official Ruby image with Node and Yarn
FROM ruby:3.1.4-slim



# Install required packages
RUN apt-get update -qq && apt-get install -y \
  build-essential \
  libpq-dev \
  nodejs \
  npm

# Install Jekyll and Bundler
RUN gem install jekyll bundler

# Create app directory
WORKDIR /srv/jekyll

# Copy the Gemfiles
COPY Gemfile* ./

# Install gems
RUN bundle install

# Copy the rest of the site
COPY . .

# Expose the port Jekyll runs on
EXPOSE 4000

# Run Jekyll server
CMD ["bundle", "exec", "jekyll", "serve", "--host", "0.0.0.0"]
